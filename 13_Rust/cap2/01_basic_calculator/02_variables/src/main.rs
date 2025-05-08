
fn compute(a: u32, b: u32) -> u32 {
    let multiplier: u32 = 2;
    let result: u32 = a * multiplier + b;
    result
}

fn compute_let(a: &str) -> String { // using &str we are using a string reference
    let result: String = a.to_string() + " World"; // to_string() convierte el string a String
    result
}

fn compute_const(a: u32, b: u32) -> u32 {
    const MULTIPLIER: u32 = 2;
    let result: u32 = a * MULTIPLIER + b;
    result
}

fn compute_const1(a: u32) -> u32 {
    const DIVISOR: u32 = 2;
    let result: u32 = a / DIVISOR;
    result
}

#[cfg(test)]
mod tests {
    use crate::compute;
    use crate::compute_let;
    use crate::compute_const;
    use crate::compute_const1;

    #[test]
    fn test_compute() {
        assert_eq!(compute(1, 2), 4);
    }

    #[test]
    fn test_compute_let() {
        assert_eq!(compute_let("Hello"), "Hello World")
    }

    #[test]
    fn test_compute_const() {
        assert_eq!(compute_const(1, 2), 4)
    }

    #[test]
    fn test_compute_const1() {
        assert_eq!(compute_const1(6), 3)
    }
}
