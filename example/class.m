class classname
  int a=0
  int b=0
  function int f(int val)
    a = val
  end
end

newclass = new classname()
newclass.a=1
newclass.f(2)
printf("%d\n", newclass.a)