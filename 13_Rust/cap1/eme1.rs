// acceder a la position numero 2 de una tupla
fn main() {
	let rs: (i32, &str, char) = (32, "Juan", 'i');
	let nombre = rs.1;
	println!("{}", nombre);
}

fn condicionales() {
	// control de flujo

	let number: i32 = 23;

	if number < 10 {
		println!("Es menor que 10");
	} else  if number == 10 {
		println!("Es igual a {}", number);
	} else {
		println!("Es mayor que 10");
	}
}

fn loop() {
	let mut contador = 0;

	loop {
		println!("Helo {}", contador);
		contador += 1;
		if contador == 3 {
			break;
		}
	}
}


fn for_r() {
	//for
	for number in 1..4 {
		println!("{} x {} = {}", number, number, (number*number));
	}
}
