int a = 1
function int compute(int a)
  a = a + 1
  return a
end
a = a + 1
compute(a)
printf("%d\n", a)