-- File: pck_myhdl_07.vhd
-- Generated by MyHDL 0.7
-- Date: Sun Dec 19 16:52:33 2010


library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

package pck_myhdl_07 is

    attribute enum_encoding: string;

    function to_std_logic (arg: boolean) return std_logic;

    function to_std_logic (arg: integer) return std_logic;

    function to_unsigned (arg: boolean; size: natural) return unsigned;

    function to_signed (arg: boolean; size: natural) return signed;

    function to_integer(arg: boolean) return integer;

    function to_integer(arg: std_logic) return integer;

    function to_unsigned (arg: std_logic; size: natural) return unsigned;

    function to_signed (arg: std_logic; size: natural) return signed;

    function to_boolean (arg: std_logic) return boolean;

    function to_boolean (arg: unsigned) return boolean;

    function to_boolean (arg: signed) return boolean;

    function to_boolean (arg: integer) return boolean;

    function "-" (arg: unsigned) return signed;

end pck_myhdl_07;


package body pck_myhdl_07 is

    function to_std_logic (arg: boolean) return std_logic is
    begin
        if arg then
            return '1';
        else
            return '0';
        end if;
    end function to_std_logic;

    function to_std_logic (arg: integer) return std_logic is
    begin
        if arg /= 0 then
            return '1';
        else
            return '0';
        end if;
    end function to_std_logic;


    function to_unsigned (arg: boolean; size: natural) return unsigned is
        variable res: unsigned(size-1 downto 0) := (others => '0');
    begin
        if arg then
            res(0):= '1';
        end if;
        return res;
    end function to_unsigned;

    function to_signed (arg: boolean; size: natural) return signed is
        variable res: signed(size-1 downto 0) := (others => '0');
    begin
        if arg then
            res(0) := '1';
        end if;
        return res; 
    end function to_signed;

    function to_integer(arg: boolean) return integer is
    begin
        if arg then
            return 1;
        else
            return 0;
        end if;
    end function to_integer;

    function to_integer(arg: std_logic) return integer is
    begin
        if arg = '1' then
            return 1;
        else
            return 0;
        end if;
    end function to_integer;

    function to_unsigned (arg: std_logic; size: natural) return unsigned is
        variable res: unsigned(size-1 downto 0) := (others => '0');
    begin
        res(0):= arg;
        return res;
    end function to_unsigned;

    function to_signed (arg: std_logic; size: natural) return signed is
        variable res: signed(size-1 downto 0) := (others => '0');
    begin
        res(0) := arg;
        return res; 
    end function to_signed;

    function to_boolean (arg: std_logic) return boolean is
    begin
        return arg = '1';
    end function to_boolean;

    function to_boolean (arg: unsigned) return boolean is
    begin
        return arg /= 0;
    end function to_boolean;

    function to_boolean (arg: signed) return boolean is
    begin
        return arg /= 0;
    end function to_boolean;

    function to_boolean (arg: integer) return boolean is
    begin
        return arg /= 0;
    end function to_boolean;

    function "-" (arg: unsigned) return signed is
    begin
        return - signed(resize(arg, arg'length+1));
    end function "-";

end pck_myhdl_07;


