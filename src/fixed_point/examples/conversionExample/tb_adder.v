module tb_adder;

reg [15:0] A;
reg [15:0] B;
wire [15:0] output2;
reg clk;
reg reset;

initial begin
    $from_myhdl(
        A,
        B,
        clk,
        reset
    );
    $to_myhdl(
        output2
    );
end

adder dut(
    A,
    B,
    output2,
    clk,
    reset
);

endmodule
