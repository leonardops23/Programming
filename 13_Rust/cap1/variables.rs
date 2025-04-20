fn ejemplo1() {
	let x: i32 = 23;
	println!("El valor es: {}", x);
}


fn imnutable() {
	//inmutable by default
	// no change you'll need mut variable
	let x: i64 = 1;
	println!("{:?}", x);
	x = 23;
	println!("{:?}", x);
}


fn mutable() {
	let mut i: i32 = 23;
	println!("{:?}", i);
	i = 1;
	println!("{:?}", i);
}

//use of let

fn main() {
	// ingora la variable y para que compile sin advertencias
	let _nombre = "rust";
	let edad: i32;
	edad = 23;

	println!("{:?}", edad);
}
