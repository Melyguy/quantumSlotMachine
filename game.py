import qsharp
from qsharp import TargetProfile

qsharp.init(target_profile=TargetProfile.Base, project_root=".")

from qsharp.code.QuantumSlotMachine import PlaySlotMachine
reels = [
        "🍒", "🍋", "🔔", "💫",
        "7️⃣", "💎", "🍀", "👑"
    ]

def result_to_symbols(bitstring):
    return [reels[int(bitstring[i:i+3], 2)] for i in range(0, len(bitstring), 3)]

def spin(mode="normal"):
    results = PlaySlotMachine(mode)  # if your Q# function supports a mode
    bitstring = ''.join('1' if r == qsharp.Result.One else '0' for r in results)



    symbol_list = [reels[int(bitstring[i:i+3], 2)] for i in range(0, len(bitstring), 3)]

    payout = evaluate_payout(bitstring, mode)

    print(f"Quantum state: {bitstring}")
    print(f"Reels: {symbol_list}")
    print(f"Payout: {payout}")

    return {
        "bitstring": bitstring,
        "symbols": symbol_list,
        "payout": payout
    }

def evaluate_payout(bitstring, mode):
    if bitstring == "111":
        return "JACKPOT"
    if bitstring.count("1") >= 2:
        return "Big win"
    if mode == "bonus":
        return "Quantum bonus"
    return "Try again"

if __name__ == "__main__":
    spin()