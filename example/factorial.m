function int factorial(int n)
  int i=0
  int result = 1
  for i=1,n+1,1
    result = result * i
  end
  return result
end

printf("%d", factorial(4))