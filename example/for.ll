; ModuleID = ""
target triple = "arm64-apple-darwin22.1.0"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

define void @"main"()
{
main.entry:
  %".2" = load i32, i32* @"i"
  %".3" = add i32 %".2", 1
  store i32 %".3", i32* @"i"
  %".5" = load i32, i32* @"i"
  store i32 1, i32* @"i"
  %".7" = load i32, i32* @"i"
  br label %".8"
.8:
  %".12" = load i32, i32* @"i"
  %".13" = icmp slt i32 %".12", 5
  br i1 %".13", label %".9", label %".10"
.9:
  %".15" = getelementptr inbounds [4 x i8], [4 x i8]* @".str0", i32 0, i32 0
  %".16" = load i32, i32* @"i"
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".15", i32 %".16")
  %".18" = add i32 %".12", 1
  store i32 %".18", i32* @"i"
  br label %".8"
.10:
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@"i" = internal global i32 0
@".str0" = constant [4 x i8] c"%d\0a\00"