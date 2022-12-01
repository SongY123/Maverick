; ModuleID = ""
target triple = "arm64-apple-darwin22.1.0"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

define void @"main"() 
{
main.entry:
  %".2" = getelementptr inbounds [3 x i8], [3 x i8]* @".str0", i32 0, i32 0
  %".3" = call i32 @"compute"(i32 10, i32 12, i32 12)
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".3")
  ret void
}

declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"scanf"(i8* %".1", ...) 

define i32 @"compute"(i32 %"a", i32 %"b", i32 %"c") 
{
compute.entry:
  %".5" = alloca i32
  store i32 %"a", i32* %".5"
  %".7" = alloca i32
  store i32 %"b", i32* %".7"
  %".9" = alloca i32
  store i32 %"c", i32* %".9"
  %".11" = load i32, i32* %".5"
  %".12" = load i32, i32* %".7"
  %".13" = add i32 %".11", %".12"
  %".14" = load i32, i32* %".9"
  %".15" = mul i32 %".13", %".14"
  ret i32 %".15"
}

@".str0" = constant [3 x i8] c"%d\00"