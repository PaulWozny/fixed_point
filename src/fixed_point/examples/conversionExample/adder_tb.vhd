-- File: adder_tb.vhd
-- Generated by MyHDL 0.10
-- Date: Mon Nov 26 11:42:33 2018


library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_010.all;

entity adder_tb is
end entity adder_tb;


architecture MyHDL of adder_tb is


signal adder0_x2: signed (11 downto 0);
signal adder0_x1: signed (16 downto 0);
signal adder0_output2: signed (16 downto 0);

begin


adder0_x2 <= to_signed(256, 12);
adder0_x1 <= to_signed(49152, 17);



adder0_output2 <= (adder0_x1 + adder0_x2);

end architecture MyHDL;
