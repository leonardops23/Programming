
// tipos escalares

// Enteros
fn integer() {
	let integer_i32: i32 = -10;
	let integer_u64: u64 = 1000;
	let integer_isize: isize = 42;

	println!("Integer i32: {}", integer_i32);
	println!("Integer u64: {}", integer_u64);
	println!("Integer isize: {}", integer_isize);
}


// Flotantes
fn main() {
	let float_f32: f32 = 3.14;
	let float_f64: f64 = 2.543;

	println!("Float f32: {}", float_f32);
	println!("Float f64: {}", float_f64);
}


// bool
fn bool() {
	let vardadero: bool = true;
	let falso: bool = false;

	println!("Vardadero: {}", vardadero);
	println!("Falso: {}", falso);
}

// Char
fn char_main() {
	let character: char = 'A';
	let mut emoji: char = ' ';
	println!("Character: {}", character);
	println!("EMoji: {}", emoji);
}


fn tuplas_main() {
	let tupla: (i32, &str, f64) = (10, "Hola", 3.14);
	println!("tupla: {:?}", tupla);
	println!("Segundo elemento: {}", tupla.1);
}

fn arr_main() {
	// arreglos
	let arreglo: [i32; 5] = [1, 2, 3, 4, 5];
	println!("Arreglo: {:?}", arreglo);
	println!("Primer elemento del arrglo {}", arreglo[0]);
}




