; ModuleID = ""
target triple = "arm64-apple-darwin22.1.0"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

define void @"main"() 
{
main.entry:
  br label %".2"
.2:
  %".6" = load i32, i32* @"i"
  %".7" = icmp slt i32 %".6", 10
  %".8" = icmp ne i1 %".7", 0
  br i1 %".8", label %".3", label %".4"
.3:
  %".10" = load i32, i32* @"i"
  %".11" = add i32 %".10", 1
  store i32 %".11", i32* @"i"
  %".13" = load i32, i32* @"i"
  %".14" = getelementptr inbounds [4 x i8], [4 x i8]* @".str0", i32 0, i32 0
  %".15" = load i32, i32* @"i"
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".14", i32 %".15")
  br label %".2"
.4:
  ret void
}

declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"scanf"(i8* %".1", ...) 

@"i" = internal global i32 0
@".str0" = constant [4 x i8] c"%d\0a\00"