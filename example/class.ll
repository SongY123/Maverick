; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

%"classname" = type <{i32, i32}>
define void @"main"()
{
main.entry:
  %"newclass" = alloca %"classname"
  %".2" = getelementptr %"classname", %"classname"* %"newclass", i32 0, i32 1
  store i32 1, i32* %".2"
  %".4" = load i32, i32* %".2"
  %".5" = getelementptr inbounds [4 x i8], [4 x i8]* @".str0", i32 0, i32 0
  %".6" = getelementptr %"classname", %"classname"* %"newclass", i32 0, i32 1
  %".7" = load i32, i32* %".6"
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".5", i32 %".7")
  %".9" = call i32 @"classname.f"(%"classname"* %"newclass", i32 2)
  %".10" = getelementptr inbounds [4 x i8], [4 x i8]* @".str1", i32 0, i32 0
  %".11" = getelementptr %"classname", %"classname"* %"newclass", i32 0, i32 1
  %".12" = load i32, i32* %".11"
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".10", i32 %".12")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"classname.f"(%"classname"* %"this", i32 %"val")
{
classname.f.entry:
  %".4" = alloca i32
  store i32 %"val", i32* %".4"
  %".6" = load i32, i32* %".4"
  %".7" = getelementptr %"classname", %"classname"* %"this", i32 0, i32 1
  store i32 %".6", i32* %".7"
  %".9" = load i32, i32* %".7"
  ret i32 0
}

@".str0" = constant [4 x i8] c"%d\0a\00"
@".str1" = constant [4 x i8] c"%d\0a\00"