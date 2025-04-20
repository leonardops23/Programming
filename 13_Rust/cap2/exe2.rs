fn main() {
	let collected_iterator: Vec<i32> = (0..19).collect();
	println!("collected (0..10) into: {:?}", collected_iterator);

	let mut xs = vec![1i32, 2, 3];
	println!("Initial vector: {:?}", xs);
	// enter new integer at the end of  the vector
	xs.push(3);

	println!("Initial vector: {:?}", xs);

}
