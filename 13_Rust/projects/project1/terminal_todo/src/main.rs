use std::io; // Necesitamos std::io para entrada/salida
use std::io::Write; // Necesitamos Write para vaciar el buffer de salida (flush)

fn main() {
    println!("¡Bienvenido a tu aplicación de lista de tareas en la terminal!");
    println!("Comandos disponibles: add <tarea>, list, exit");

    // Vec es un vector (una lista redimensionable) que almacenará nuestras tareas como String
    let mut todos: Vec<String> = Vec::new();

    // Este es el bucle principal de la aplicación
    loop {
        // 1. Mostrar el prompt al usuario
        print!("> ");
        // Aseguramos que el prompt se muestre inmediatamente en la terminal
        io::stdout().flush().expect("Error al vaciar el buffer");

        // 2. Leer la línea de entrada del usuario
        let mut input = String::new(); // Creamos una String mutable para guardar la entrada
        io::stdin().read_line(&mut input) // Leemos la línea completa hasta el salto de línea
            .expect("Error al leer la línea"); // Manejo básico de errores: si falla, el programa colapsa

        // Eliminar espacios en blanco al principio y al final de la entrada
        let input = input.trim();

        // 3. Procesar el comando
        // Dividimos la entrada en palabras/partes
        let parts: Vec<&str> = input.split_whitespace().collect();

        // Verificamos la primera parte (el comando)
        if let Some(command) = parts.first() {
            match *command { // Usamos match para manejar diferentes comandos
                "add" => {
                    // El comando es "add". El resto de las partes es la descripción de la tarea.
                    let task_description = parts[1..].join(" "); // Unimos las partes restantes
                    if task_description.is_empty() {
                        println!("Uso: add <tarea>");
                    } else {
                        todos.push(task_description); // Agregamos la tarea al vector
                        println!("Tarea agregada.");
                    }
                }
                "list" => {
                    // El comando es "list".
                    println!("--- Tus Tareas ---");
                    if todos.is_empty() {
                        println!("No hay tareas todavía.");
                    } else {
                        // Iteramos sobre el vector para mostrar cada tarea con su índice
                        for (index, task) in todos.iter().enumerate() {
                            println!("{}. {}", index + 1, task); // Mostramos índice + 1 para que empiece en 1
                        }
                    }
                    println!("------------------");
                }
                "exit" => {
                    // El comando es "exit". Salimos del bucle.
                    println!("¡Adiós!");
                    break; // Rompe el bucle principal, terminando el programa
                }
                "" => {
                    // La entrada estaba vacía, no hacemos nada
                }
                _ => {
                    // Cualquier otro comando es desconocido
                    println!("Comando desconocido: '{}'. Comandos disponibles: add <tarea>, list, exit", command);
                }
            }
        } else {
            // La entrada estaba vacía (solo espacios o nada)
        }
    }
}
