extern crate crypto;
use self::crypto::digest::Digest;

use self::crypto::md5::Md5;

static INPUT: &'static str = "bgvyzdsv";

fn find_md5_value(input: &str, start: u32, pattern: &str) -> u32 {
    let mut hash = Md5::new();
    let mut i: u32 = start;

    // Similar to the python implementation
    loop {
        hash.input_str(&format!("{}{:?}", input, i));

        if hash.result_str().starts_with(pattern) {
            return i;
        } else {
            hash.reset();
            i += 1;
        }
    }
}

fn main() {
    let answer_one: u32 = find_md5_value(INPUT, 0, "00000");
    // We don't need to start from 0 again since we know where we left off
    let answer_two: u32 = find_md5_value(INPUT, answer_one, "000000");
    println!("{}", answer_one);
    println!("{}", answer_two);
}
