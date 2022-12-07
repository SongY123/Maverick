; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

define void @"main"()
{
main.entry:
  %".2" = getelementptr inbounds [10 x i32], [10 x i32]* @"arr", i32 0, i32 9
  store i32 90, i32* %".2"
  %".4" = load i32, i32* %".2"
  %".5" = getelementptr inbounds [8 x i8], [8 x i8]* @".str0", i32 0, i32 0
  %".6" = getelementptr inbounds [10 x i32], [10 x i32]* @"arr", i32 0, i32 0
  %".7" = load i32, i32* %".6"
  %".8" = getelementptr inbounds [10 x i32], [10 x i32]* @"arr", i32 0, i32 9
  %".9" = load i32, i32* %".8"
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".5", i32 %".7", i32 %".9")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@"arr" = internal global [10 x i32] undef
@".str0" = constant [8 x i8] c"%d, %d\0a\00"