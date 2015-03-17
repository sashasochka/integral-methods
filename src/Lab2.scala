import scala.io.Source

object Lab2 extends App {
  type Vector = Seq[Double]
  type Matrix = Seq[Vector]

  def printAb(msg: String = "") = {
    if (msg.nonEmpty) println(s"$msg: ")
    for (line <- Ab) {
      for (elem <- line) print(f"$elem%16.10f,")
      println()
    }
    println()
  }

  def printVec(A: Vector) =
    for (v <- A)
      print(f"\t$v%12.7f")


  def printVecExp(A: Vector) =
    for (v <- A)
      print(f"\t$v%9.1E")


  def *(A: Matrix, B: Matrix): Matrix = {
    for (i <- 0 until N) yield {
      for (k <- 0 until N) yield {
        A(i).zipWithIndex.map({ case (a, j) => a * B(j)(k)}).sum
      }
    }
  }

  def mul(A: Matrix, b: Vector): Vector =
    for (i <- 0 until N) yield
      A(i).zip(b).map(p => p._1 * p._2).sum

  def minus(a: Vector, b: Vector) =
    0.until(N).map(i => a(i) - b(i))


  val N = 4
  val Ab =
    for (line <- Source.fromFile("input/lab2.txt").getLines().toArray) yield
      for (word <- line split ' ') yield word.toDouble

  val A: Matrix = Ab.map(_.init.toSeq).toSeq
  val b: Vector = Ab.map(_.last).toSeq

  var x: Vector = b
  def iter(step: Int = 0) {
    val newX = new Array[Double](N)
    for (i <- 0 until N) {
      for (j <- 0.to(i - 1)) {
        newX(i) -= A(i)(j) / A(i)(i) * newX(j)
      }

      for (j <- i + 1 until N) {
        newX(i) -= A(i)(j) / A(i)(i) * x(j)
      }

      newX(i) += b(i) / A(i)(i)
    }

    print(f"Step $step%3d: ")
    printVec(x)
    print(";  ")
    print(s"Вектор нев’язки: ")
    printVecExp(minus(mul(A, newX), b))
    println()

    val end = newX.zip(x).map({
      case (q, w) => math.abs(q - w)
    }).max < 1e-7

    if (end) {

      x = newX
      return
    }

    x = newX
    iter(step + 1)
  }

  iter()
}
