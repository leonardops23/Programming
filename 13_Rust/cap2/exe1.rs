

// declarar una variable mutable y asignar un valor

fn main() {
	let name: &str;
	let mut edad: i32 = 23;
	name = "Ivan";
	edad += 1;
	// is student
	let is_student: bool = false;

	if is_student {
		println!("{name} tengo {edad} y si soy estudiante", );
	} else {
		println!("{name} tengo {edad} y no soy estudiante", );
	}

}
