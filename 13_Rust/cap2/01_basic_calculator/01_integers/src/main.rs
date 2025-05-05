
fn compute(a: u32, b: u32) -> u32 {
   let multiplier: u32 = 2;
   a * multiplier + b
}

#[cfg(test)]
mod tests {
    use crate::compute; // import the compute function

    #[test]
    fn test_compute() {
        assert_eq!(compute(1, 2), 4);
    }

    #[test]
    fn test_compute_with_multiplier() {
        assert_eq!(compute(1, 2), 4);
    }
}
