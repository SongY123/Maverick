class classname
  int a
  int b
  function int f(int val)
    a = val
  end
end

newclass = new classname()
newclass.a=1
newclass.f(2)
printf("%d\n", newclass.a)