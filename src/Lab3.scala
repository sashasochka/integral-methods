import scala.io.Source

object Lab3 extends App {
  type Vec = Seq[Double]
  type Matrix = Seq[Vec]

  def printMatrix(A: Matrix, msg: String = "") = {
    if (msg.nonEmpty) println(s"$msg: ")
    for (line <- A) {
      for (elem <- line) print(f"$elem%16.10f,")
      println()
    }
    println()
  }

  def mul(A: Matrix, B: Matrix): Matrix = {
    for (i <- 0 until N) yield {
      for (k <- 0 until N) yield {
        A(i).zipWithIndex.map({ case (a, j) => a * B(j)(k)}).sum
      }
    }
  }


  val N = 4

  var A: Matrix =
    for (line <- Source.fromFile("input/lab3.txt").getLines().toVector) yield
      for (word <- line.split(' ').toVector) yield word.toDouble

  for (i <- 0 until N - 1) {
    def MInv(row: Int): Matrix = {
      val NC = row - 1
      for (j <- 0 until N) yield j match {
        case NC => A(row)
        case _ => (Vector.fill(j)(0.0) :+ 1.0) ++ Vector.fill(N - j - 1)(0.0)
      }
    }

    def M(row: Int): Matrix = {
      val NC = row - 1
      for (j <- 0 until N) yield j match {
        case NC => A(row).zipWithIndex.map {
          case (v, NC) => 1.0 / A(row)(NC)
          case (v, col) => -v / A(row)(NC)
        }
        case _ => (Vector.fill(j)(0.0) :+ 1.0) ++ Vector.fill(N - j - 1)(0.0)
      }
    }

    val minv = MInv(N - i - 1)
    val m = M(N - i - 1)
    A = mul(mul(minv, A), m)

    printMatrix(minv, "MInv")
    printMatrix(m, "M")
    printMatrix(A, "A")
  }
}
