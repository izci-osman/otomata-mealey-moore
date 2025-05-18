def read_input_file(filename):
    with open(filename, 'r') as file:
        data = file.read().splitlines()
    return data

def parse_states(data):
    states_line = data[0].replace("Q:", "").replace("{", "").replace("}", "").strip()
    states = states_line.split(",")
    return [state.strip() for state in states]

def parse_alphabet(data):
    alphabet_line = data[1].replace("S=", "").replace("{", "").replace("}", "").strip()
    alphabet = alphabet_line.split(",")
    return [symbol.strip() for symbol in alphabet]

def parse_output_alphabet(data):
    output_alphabet = data[2].replace("Γ=", "").replace("{", "").replace("}", "").strip().split(",")
    return [output.strip() for output in output_alphabet]

def parse_transition_table(filename):
    transition_table = {}
    with open(filename, 'r') as file:
        data = file.read().splitlines()[1:]
        for line in data:
            parts = line.split("\t")
            if len(parts) >= 3:
                state = parts[0].strip()
                transitions = [parts[1].strip(), parts[2].strip()]
                transition_table[state] = transitions
            else:
                print(f"Uyarı: Eksik veri veya TAB karakteri eksik - {line}")
    return transition_table

def parse_output_table(filename):
    output_table = {}
    with open(filename, 'r') as file:
        data = file.read().splitlines()[1:]
        for line in data:
            parts = line.split("\t")
            if len(parts) >= 2:
                state = parts[0].strip()
                output = parts[1].strip()
                output_table[state] = output
            else:
                print(f"Uyarı: Eksik veri satırı - {line}")
    return output_table

def moore_machine_simulation(states, alphabet, input_string, transition_table, output_table):
    current_state = states[0]
    outputs = []

    for symbol in input_string:
        if symbol not in alphabet:
            print(f"Geçersiz sembol: {symbol}")
            return
        state_index = alphabet.index(symbol)

        if current_state in transition_table:
            next_state = transition_table[current_state][state_index]
            current_state = next_state
        else:
            print(f"Uyarı: '{current_state}' durumu geçiş tablosunda bulunamadı.")
            return

        if current_state in output_table:
            outputs.append(output_table[current_state])
        else:
            print(f"Uyarı: '{current_state}' durumu için çıkış bulunamadı.")
            return

    print("Geçilen Durumlar: ", " -> ".join(outputs))
    print("Nihai Çıktı: ", outputs[-1] if outputs else "Yok")

def main():
    input_data = read_input_file("INPUT.TXT")
    states = parse_states(input_data)
    alphabet = parse_alphabet(input_data)
    output_alphabet = parse_output_alphabet(input_data)

    transition_table = parse_transition_table("GECISTABLOSU.TXT")
    output_table = parse_output_table("OUTPUT.TXT")

    print("Alphabet:", alphabet)
    input_string = input("Giriş dizisini giriniz: ")
    moore_machine_simulation(states, alphabet, input_string, transition_table, output_table)

if __name__ == "__main__":
    main()
