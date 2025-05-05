
fn compute(a: u32, b: u32) -> u32 {
    let multiplier: u32 = 2;
    let result: u32 = a * multiplier + b;
    result
}

#[cfg(test)]
mod tests {
    use crate::compute;

    #[test]
    fn test_compute() {
        assert_eq!(compute(1, 2), 4);
    }

    #[test]
    fn test_compute_with_multiplier() {
        assert_eq!(compute(3, 2), 8);
    }

    #[test]
    fn test_compute_with_multiplier_and_addition() {
        assert_eq!(compute(3, 2), 8);
    }

    #[test]
    fn test_compute_with_multiplier_and_addition_and_subtraction() {
        assert_eq!(compute(3, 2), 8);
    }
}
