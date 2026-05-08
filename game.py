import qsharp
from qsharp import TargetProfile

qsharp.init(target_profile=TargetProfile.Base, project_root=".")

from qsharp.code.QuantumSlotMachine import PlaySlotMachine

symbols = {
    "000": "🍒",
    "001": "🍋",
    "010": "🔔",
    "011": "💫",
    "100": "7️⃣",
    "101": "💎",
    "110": "🍀",
    "111": "👑"
}

def result_to_symbols(bitstring):
    return [symbols[bitstring[i:i+3]] for i in range(0, len(bitstring), 3)]

def spin():
    results = PlaySlotMachine()

    bitstring = ''.join('1' if r == qsharp.Result.One else '0' for r in results)

    symbol_list = result_to_symbols(bitstring)

    print(f"Quantum Bits: {bitstring}")
    print(f"Result: {''.join(symbol_list)}")

if __name__ == "__main__":
    spin()  