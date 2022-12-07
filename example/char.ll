; ModuleID = ""
target triple = "arm64-apple-darwin22.1.0"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

define void @"main"()
{
main.entry:
  %".2" = getelementptr inbounds [3 x i8], [3 x i8]* @".str0", i32 0, i32 0
  %".3" = load i8, i8* @"c"
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".2", i8 %".3")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@"c" = internal global i8 99
@".str0" = constant [3 x i8] c"%c\00"