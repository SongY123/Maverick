; ModuleID = ""
target triple = "arm64-apple-darwin22.1.0"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

define void @"main"() 
{
main.entry:
  store i32 0, i32* @"a"
  %".3" = load i32, i32* @"a"
  ret void
}

declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"scanf"(i8* %".1", ...) 

@"a" = internal global i32 2