; ModuleID = ""
target triple = "arm64-apple-darwin22.1.0"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

define void @"main"() 
{
main.entry:
  %".2" = getelementptr inbounds [16 x i8], [16 x i8]* @".str0", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2")
  %".4" = getelementptr inbounds [3 x i8], [3 x i8]* @".str1", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"scanf"(i8* %".4", i32* @"b")
  %".6" = getelementptr inbounds [20 x i8], [20 x i8]* @".str2", i32 0, i32 0
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6")
  %".8" = getelementptr inbounds [4 x i8], [4 x i8]* @".str3", i32 0, i32 0
  %".9" = load i32, i32* @"a"
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".8", i32 %".9")
  %".11" = getelementptr inbounds [20 x i8], [20 x i8]* @".str4", i32 0, i32 0
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11")
  %".13" = getelementptr inbounds [4 x i8], [4 x i8]* @".str5", i32 0, i32 0
  %".14" = load i32, i32* @"b"
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".13", i32 %".14")
  ret void
}

declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"scanf"(i8* %".1", ...) 

@"a" = internal global i32 10
@"b" = internal global i32 12
@".str0" = constant [16 x i8] c"Please input b:\00"
@".str1" = constant [3 x i8] c"%d\00"
@".str2" = constant [20 x i8] c"The value of a is :\00"
@".str3" = constant [4 x i8] c"%d\0a\00"
@".str4" = constant [20 x i8] c"The value of b is :\00"
@".str5" = constant [4 x i8] c"%d\0a\00"