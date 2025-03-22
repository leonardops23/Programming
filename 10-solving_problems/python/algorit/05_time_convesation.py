
def diferencia_tiempo(time1: str, time2: str) -> str:
    """
    
    """
    try:
        h1, m1, s1 = map(int, time1.split(':'))
        h2, m2, s2 = map(int, time2.split(':'))
    
        total_second1 = (h1 * 3600) + (m1 * 60) + s1
        total_second2 = (h2 * 3600) + (m2 * 60) + s2

        return total_second2 - total_second1
    

    except (ValueError, IndexError):
        return None



print(diferencia_tiempo("01:00:00", "01:00:10"))  # Debe imprimir 10
print(diferencia_tiempo("00:00:00", "01:00:00"))  # Debe imprimir 3600
print(diferencia_tiempo("01:01:01", "02:02:02"))  # Debe imprimir 3661
print(diferencia_tiempo("01:01:01", "02:02")) # D
