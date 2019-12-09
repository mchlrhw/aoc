use std::convert::TryFrom;

use fehler::{throw, throws};
use thiserror;

#[derive(Debug, thiserror::Error)]
pub enum Error {
    #[error("no opcode for {0}")]
    InvalidOpCode(u64),
    #[error("failed to load program")]
    LoadError(#[from] std::num::ParseIntError),
    #[error("missing args for {op:?} at {idx}")]
    MissingArg { op: OpCode, idx: u64 },
    #[error("missing operands for {op:?} at {pc}")]
    MissingOperands { op: OpCode, pc: usize },
}

#[derive(Clone, Copy, Debug, PartialEq)]
pub enum OpCode {
    Add = 1,
    Mul,
    End = 99,
}

impl TryFrom<u64> for OpCode {
    type Error = Error;

    #[throws(Self::Error)]
    fn try_from(v: u64) -> Self {
        match v {
            x if x == Self::Add as u64 => Self::Add,
            x if x == Self::Mul as u64 => Self::Mul,
            x if x == Self::End as u64 => Self::End,
            x => throw!(Self::Error::InvalidOpCode(x)),
        }
    }
}

#[throws(Error)]
pub fn compute(mut program: Vec<u64>) -> Vec<u64> {
    // program counter
    let mut pc = 0;

    loop {
        let current_state = program.clone();

        let op = OpCode::try_from(current_state[pc])?;

        if op == OpCode::End {
            break;
        }

        let indices = current_state
            .get(pc + 1..=pc + 3)
            .ok_or(Error::MissingOperands { op, pc })?;
        let (arg_0_idx, arg_1_idx, res_idx) = (indices[0], indices[1], indices[2]);

        let arg_0 = current_state
            .get(arg_0_idx as usize)
            .ok_or(Error::MissingArg { op, idx: arg_0_idx })?;
        let arg_1 = current_state
            .get(arg_1_idx as usize)
            .ok_or(Error::MissingArg { op, idx: arg_1_idx })?;

        let res = match op {
            OpCode::Add => arg_0 + arg_1,
            OpCode::Mul => arg_0 * arg_1,
            _ => unreachable!(),
        };

        program[res_idx as usize] = res;

        pc += 4;
    }

    program
}

pub fn load(program: &str) -> Result<Vec<u64>, Error> {
    program
        .split(',')
        .map(|s| s.trim().parse::<u64>().map_err(|e| e.into()))
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest_parametrize;

    #[rstest_parametrize(
        program,
        expected,
        case(
            vec![1,9,10,3,2,3,11,0,99,30,40,50],
            vec![3500,9,10,70,2,3,11,0,99,30,40,50],
        ),
        case(vec![1,0,0,0,99], vec![2,0,0,0,99]),
        case(vec![2,3,0,3,99], vec![2,3,0,6,99]),
        case(vec![2,4,4,5,99,0], vec![2,4,4,5,99,9801]),
        case(vec![1,1,1,4,99,5,6,0,99], vec![30,1,1,4,2,5,6,0,99]),
    )]
    #[throws(Error)]
    #[allow(unused)]
    fn compute_examples(program: Vec<u64>, expected: Vec<u64>) {
        let output = compute(program)?;
        assert_eq!(output, expected);
    }

    #[rstest_parametrize(
        program,
        expected,
        case("1,9,10,3,2,3,11,0,99,30,40,50", vec![1,9,10,3,2,3,11,0,99,30,40,50]),
        case("1,0,0,0,99", vec![1,0,0,0,99]),
        case("2,3,0,3,99", vec![2,3,0,3,99]),
        case("2,4,4,5,99,0", vec![2,4,4,5,99,0]),
        case("1,1,1,4,99,5,6,0,99", vec![1,1,1,4,99,5,6,0,99]),
    )]
    #[throws(Error)]
    #[allow(unused)]
    fn load_examples(program: &str, expected: Vec<u64>) {
        let output = load(program)?;
        assert_eq!(output, expected)
    }

    #[test]
    #[throws(Error)]
    #[allow(unused)]
    fn part_1_solution() {
        let puzzle_input = String::from_utf8_lossy(include_bytes!("day_02/input.txt"));
        let mut program = load(&puzzle_input)?;

        // adjust initial state as per instructions
        program[1] = 12;
        program[2] = 2;

        let final_state = compute(program)?;
        let result = final_state[0];

        assert_eq!(result, 2782414);
    }

    #[test]
    #[throws(Error)]
    #[allow(unused)]
    fn part_2_solution() {
        let puzzle_input = String::from_utf8_lossy(include_bytes!("day_02/input.txt"));

        let mut noun = 0;
        let mut verb = 0;

        'out: for a in 0..=99 {
            for b in 0..=99 {
                let mut program = load(&puzzle_input)?;
                program[1] = a;
                program[2] = b;

                let final_state = compute(program)?;
                let result = final_state[0];
                if result == 19690720 {
                    noun = a;
                    verb = b;
                    break 'out;
                }
            }
        }

        let answer = 100 * noun + verb;

        assert_eq!(answer, 9820);
    }
}
