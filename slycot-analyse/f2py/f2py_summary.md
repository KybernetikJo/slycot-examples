FWIW, I have done some background reading about F2PY, and this is my current understanding. I am a newbie to fortran, therefore you should take this with a bit of toast.

The stable version of  [f2py stable](https://numpy.org/doc/stable/f2py/) do have some duplication in the documentation.
I fixed that, so the dev version [f2py dev](https://numpy.org/devdocs/f2py/index.html) is a better read.
The online "book" [python fortran](https://pnavaro.github.io/python-fortran/01.f2py.html) can also be helpful.
The f2py was design with Fortran90/95 in mind. 
The goal of F2PY is, to make the use of Fortran in Python easy, and to make the API `PYTHONIC`. The behavior of F2PY depends heavily on the data types used in the Fortran procedures, the data types used in Python and on the F2PY signature (none, infile.f or .pyf). Therefore, very simple conclusions cannot be drawn, some understanding of Fortran seems to be necessary and good templates might be helpful.

First, Fortran has two procedures, subroutines and functions. (This effects the F2PY signature file pyf)
Both subroutines and functions have access to variables in the parent scope by argument association, 
this is similar to call by reference.

All arguments in Fortran77 can be seen as call by reference, by default. 

In Fortran90/95 the `intent attribute` has been introduced `intent(in), intent(out), intent(inout)`. This allows the compiler to check for unintentional errors and provides self-documentation (in Fortran77 the API was only documented in comments). In addition, some compilers can do code optimization based on intent, mabye?. [Is there performance advantage of using intent(in) and intent(out)?](https://fortran-lang.discourse.group/t/is-there-performance-advantage-of-using-intent-in-and-intent-out/1660)


**intent in Fortran90/95**
[Writing fast Fortran routines for Python](https://sites.engineering.ucsb.edu/~shell/che210d/f2py.pdf)

`intent(in)`: The variable is an input to the subroutine only. Its value
must not be changed during the course of the subroutine.

`intent(out)`: The variable is an output from the subroutine only. Its
input value is irrelevant. We must assign this variable a
value before exiting the subroutine.

`intent(inout)`: The subroutine both uses and modifies the data in the
variable. Thus, the initial value is sent and we ultimately
make modifications base on it.

In Fortran there is also the concept of a `pure function`, which do not have side effects. [What is a pure function?](https://fortran-lang.discourse.group/t/what-is-a-pure-function/4654)
In Fortran90/95 a new keyword `pure` was introduced.

In Fortran2003 a `value attribute` has been introduced. Now call by value is possible. F2PY do not have a good support of Fortran2003 features, so it can be mostly ignored.

