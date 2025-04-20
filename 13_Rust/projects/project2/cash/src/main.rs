use std::io;
use std::io::Write; // Import Write for flush

fn main() {
    // tenemos un menu de optiones, las principlaes son depositar la cuenta, ver en la cuenta
    // salir de deposito
    print!("==== Bienvenido a BankDev ====\n"); // Moved welcome message outside the loop
    chosen_option();
}


fn chosen_option() {

    let menu: [&str; 4] = [
        "1. Consultar saldo",
        "2. Realizar Transaccion", // Assuming this means deposit or withdrawal within a transaction concept
        "3. Retirar saldo", // Or maybe "Realizar Transaccion" is just general, and withdraw is separate? Let's keep it as in the original menu for now.
        "4. Salir", // Changed "exit" to "Salir" for consistency with Spanish menu
    ];

    // Simple balance simulation
    let mut balance: f64 = 1000.0; // Example initial balance

    loop {
        // bucle para mostrar por consola las optiones de menu
        println!("\nPor favor, elija una opción:"); // Prompt the user
        for option in menu.iter() { // Iterate over menu items
            println!("{}", option);
        }

        print!("> ");
        io::stdout().flush().unwrap(); // Ensure the prompt is displayed before reading input

        let mut choice = String::new();
        io::stdin().read_line(&mut choice).expect("Error al leer la línea");

        let choice = choice.trim(); // Remove leading/trailing whitespace and the newline character

        match choice {
            "1" => {
                println!("Su saldo actual es: ${:.2}", balance); // Display balance with 2 decimal places
            }
            "2" => {
                println!("Opción no implementada: Realizar Transacción");
                // Here you would add logic for transactions (deposit, etc.)
                // Example: call a deposit function
                // balance = deposit(balance);
            }
            "3" => {
                println!("Opción no implementada: Retirar Saldo");
                 // Here you would add logic for withdrawals
                // Example: call a withdraw function
                // balance = withdraw(balance);
            }
            "4" | "exit" => { // Allow both "4" and "exit" to quit
                println!("Gracias por usar BankDev. ¡Hasta luego!");
                break; // Exit the loop
            }
            _ => {
                println!("Opción no válida. Por favor, intente de nuevo.");
            }
        }
    }
}
