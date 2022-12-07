; ModuleID = ""
target triple = "arm64-apple-darwin22.1.0"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

define void @"main"()
{
main.entry:
  %".2" = getelementptr inbounds [3 x i8], [3 x i8]* @".str0", i32 0, i32 0
  %".3" = call i32 @"factorial"(i32 4)
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".3")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"factorial"(i32 %"n")
{
factorial.entry:
  %".3" = alloca i32
  store i32 %"n", i32* %".3"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"result" = alloca i32
  store i32 1, i32* %"result"
  store i32 1, i32* %"i"
  %".8" = load i32, i32* %"i"
  br label %".9"
.9:
  %".13" = load i32, i32* %"i"
  %".14" = load i32, i32* %".3"
  %".15" = add i32 %".14", 1
  %".16" = icmp slt i32 %".13", %".15"
  br i1 %".16", label %".10", label %".11"
.10:
  %".18" = load i32, i32* %"result"
  %".19" = load i32, i32* %"i"
  %".20" = mul i32 %".18", %".19"
  store i32 %".20", i32* %"result"
  %".22" = load i32, i32* %"result"
  %".23" = add i32 %".13", 1
  store i32 %".23", i32* %"i"
  br label %".9"
.11:
  %".26" = load i32, i32* %"result"
  ret i32 %".26"
}

@".str0" = constant [3 x i8] c"%d\00"