// TODO: fix the function signature below to make the tests pass.
//  Make sure to read the compiler error message—the Rust compiler is your pair programming
//  partner in this course and it'll often guide you in the right direction!
//
// The input parameters should have the same type of the return type.
fn compute(a: i32, b: i32) -> i32 {
    // i32 is the type of the input parameters and the return type.
    // Don't touch the function body.
    a + b * 2 // 2 + 2 * 2 = 6
}

#[cfg(test)] // cfg(test) is a macro that is used to conditionally compile code.
mod tests {
    use crate::compute;

    #[test] // test is a macro that is used to mark a function as a test.
    fn case() {
        assert_eq!(compute(1, 2), 5); // assert_eq! is a macro that is used to assert that two values are equal.
    }

    #[test]
    fn case2() {
        assert_eq!(compute(2, 2), 6);
    }

    #[test]
    fn case3() {
        assert_eq!(compute(-1, 2), 3);
    }
}
