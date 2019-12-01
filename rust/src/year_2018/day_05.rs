pub fn react_polymer(polymer: &str) -> String {
    let mut buf = String::new();

    for unit in polymer.chars() {
        if let Some(prev_unit) = buf.pop() {
            let unit_lower = unit.to_lowercase().to_string();
            let prev_lower = prev_unit.to_lowercase().to_string();
            if unit == prev_unit || unit_lower != prev_lower {
                buf.extend(&[prev_unit, unit]);
            };
        } else {
            buf.extend(&[unit]);
        };
    }

    buf
}

#[cfg(test)]
mod tests {
    extern crate rstest;

    use super::*;
    use rstest::rstest_parametrize;

    #[rstest_parametrize(
        polymer,
        expected,
        case("aA", ""),
        case("abBA", ""),
        case("abAB", "abAB"),
        case("aabAAB", "aabAAB"),
        case("dabAcCaCBAcCcaDA", "dabCBAcaDA")
    )]
    fn react_polymer_examples(polymer: &str, expected: &str) {
        let reacted = react_polymer(polymer);

        assert_eq!(&reacted, expected);
    }
}
