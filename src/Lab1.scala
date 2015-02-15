import scala.io.Source

object Lab1 extends App {
  def printAb(msg: String = "") = {
    if (msg.nonEmpty) println(s"$msg: ")
    for (line <- Ab) {
      for (elem <- line) print(f"$elem%16.10f,")
      println()
    }
    println()
  }

  val N = 5
  val Ab =
    for (line <- Source.fromFile("input/lab1.txt").getLines().toArray) yield
      for (word <- line split ' ') yield word.toDouble

  printAb("Matrix read")

  for (majorRowIndex <- 0 until N - 1) {
    println(s"Straight move #${majorRowIndex + 1}")

    val bestIndex = 0.until(N)
      .map(j => (Ab(j)(majorRowIndex), majorRowIndex))
      .sortBy(x => math.abs(x._1))
      .head._2

    println(s"Swapped rows ${majorRowIndex + 1} and ${bestIndex + 1}")
    val row = Ab(majorRowIndex)
    Ab(majorRowIndex) = Ab(bestIndex)
    Ab(bestIndex) = row

    for (row <- Ab.drop(majorRowIndex + 1)) {
      val k = row(majorRowIndex) / Ab(majorRowIndex)(majorRowIndex)
      for ((el, colIndex) <- row.zipWithIndex)
        row(colIndex) -= Ab(majorRowIndex)(colIndex) * k
    }

    printAb()
  }

  for (majorIndex <- N - 1 to 1 by -1) {
    for (rowIndex <- 0 until majorIndex) {
      Ab(rowIndex)(N) -= Ab(majorIndex)(N) / Ab(majorIndex)(majorIndex) * Ab(rowIndex)(majorIndex)
      Ab(rowIndex)(majorIndex) = 0
    }
    printAb(s"Backward move #${N - majorIndex}")
  }

  printAb("Resulting matrix")

  println("X = ")
  for ((row, index) <- Ab.zipWithIndex)
    println(f"${row.last / row(index)}%.10f")
}
