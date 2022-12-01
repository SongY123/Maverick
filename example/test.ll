; ModuleID = ""
target triple = "arm64-apple-darwin22.1.0"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

define void @"main"() 
{
main.entry:
  br label %".2"
.2:
  %".7" = icmp eq i32 1, 2
  %".8" = icmp ne i1 %".7", 0
  br i1 %".8", label %".5", label %".6"
.3:
  ret void
.5:
  %".10" = getelementptr inbounds [3 x i8], [3 x i8]* @".str0", i32 0, i32 0
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i32 1)
  br label %".3"
.6:
  %".15" = icmp eq i32 1, 2
  %".16" = icmp ne i1 %".15", 0
  br i1 %".16", label %".13", label %".14"
.13:
  %".18" = getelementptr inbounds [3 x i8], [3 x i8]* @".str1", i32 0, i32 0
  %".19" = call i32 (i8*, ...) @"printf"(i8* %".18", i32 2)
  br label %".3"
.14:
  %".21" = getelementptr inbounds [3 x i8], [3 x i8]* @".str2", i32 0, i32 0
  %".22" = call i32 (i8*, ...) @"printf"(i8* %".21", i32 3)
  br label %".3"
}

declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"scanf"(i8* %".1", ...) 

@".str0" = constant [3 x i8] c"%d\00"
@".str1" = constant [3 x i8] c"%d\00"
@".str2" = constant [3 x i8] c"%d\00"