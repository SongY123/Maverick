; ModuleID = ""
target triple = "arm64-apple-darwin22.1.0"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

define void @"main"() 
{
main.entry:
  %".2" = getelementptr inbounds [3 x i8], [3 x i8]* @".str0", i32 0, i32 0
  %".3" = call i32 @"sum"(i32 10, i32 12)
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".3")
  ret void
}

declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"scanf"(i8* %".1", ...) 

define i32 @"sum"(i32 %"a", i32 %"b") 
{
sum.entry:
  %".4" = alloca i32
  store i32 %"a", i32* %".4"
  %".6" = alloca i32
  store i32 %"b", i32* %".6"
  %"a.1" = alloca i32
  store i32 10, i32* %"a.1"
  %"b.1" = alloca i32
  store i32 20, i32* %"b.1"
  %".10" = load i32, i32* %".4"
  %".11" = load i32, i32* %".6"
  %".12" = mul i32 %".10", %".11"
  ret i32 %".12"
}

@".str0" = constant [3 x i8] c"%d\00"