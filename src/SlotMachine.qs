namespace QuantumSlotMachine {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;

    operation PlaySlotMachine() : Result[] {
        use qubits = Qubit[3];

        for q in qubits {
            H(q);
        }

        mutable results = [];

        for q in qubits {
            set results += [M(q)];
        }
        ResetAll(qubits);

        return results;
    
    }
}