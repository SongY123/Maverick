; ModuleID = ""
target triple = "arm64-apple-darwin22.1.0"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

define void @"main"() 
{
main.entry:
  br label %".2"
.2:
  %".7" = load i32, i32* @"i"
  %".8" = icmp eq i32 %".7", 10
  %".9" = icmp ne i1 %".8", 0
  br i1 %".9", label %".5", label %".6"
.3:
  ret void
.5:
  %".11" = getelementptr inbounds [9 x i8], [9 x i8]* @".str0", i32 0, i32 0
  %".12" = load i32, i32* @"i"
  %".13" = icmp eq i32 %".12", 10
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".11", i1 %".13")
  br label %".3"
.6:
  %".16" = getelementptr inbounds [10 x i8], [10 x i8]* @".str1", i32 0, i32 0
  %".17" = load i32, i32* @"i"
  %".18" = icmp eq i32 %".17", 10
  %".19" = call i32 (i8*, ...) @"printf"(i8* %".16", i1 %".18")
  br label %".3"
}

declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"scanf"(i8* %".1", ...) 

@"i" = internal global i32 1
@".str0" = constant [9 x i8] c"True %d\0a\00"
@".str1" = constant [10 x i8] c"False %d\0a\00"