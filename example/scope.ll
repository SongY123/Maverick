; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

define void @"main"()
{
main.entry:
  %".2" = load i32, i32* @"a"
  %".3" = add i32 %".2", 1
  store i32 %".3", i32* @"a"
  %".5" = load i32, i32* @"a"
  %".6" = load i32, i32* @"a"
  %".7" = call i32 @"compute"(i32 %".6")
  %".8" = getelementptr inbounds [4 x i8], [4 x i8]* @".str0", i32 0, i32 0
  %".9" = load i32, i32* @"a"
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".8", i32 %".9")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@"a" = internal global i32 1
define i32 @"compute"(i32 %"a")
{
compute.entry:
  %".3" = alloca i32
  store i32 %"a", i32* %".3"
  %".5" = load i32, i32* %".3"
  %".6" = add i32 %".5", 1
  store i32 %".6", i32* %".3"
  %".8" = load i32, i32* %".3"
  %".9" = load i32, i32* %".3"
  ret i32 %".9"
}

@".str0" = constant [4 x i8] c"%d\0a\00"