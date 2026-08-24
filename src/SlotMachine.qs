namespace QuantumSlotMachine {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;

    operation PlaySlotMachine() : Result[] {
        use qubits = Qubit[3];

        H(qubits[0]);
        Rz(0.7, qubits[0]);   // phase shift
        H(qubits[0]);

        H(qubits[1]);
        H(qubits[2]);

        CNOT(qubits[0], qubits[1]);
        CNOT(qubits[1], qubits[2]);

        mutable results = [];

        for q in qubits {
            set results += [M(q)];
        }
        ResetAll(qubits);

        return results;
    
    }
}