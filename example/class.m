class classname
  int a=0
  int b=0
  function int f(int val)
    b = val
    return b
  end
end

classname newclass = new classname()
newclass.b=1
printf("%d\n", newclass.b)
newclass.f(2)
printf("%d\n", newclass.b)