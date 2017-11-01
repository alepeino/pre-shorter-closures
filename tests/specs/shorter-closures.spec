--DESCRIPTION--

Test short closure macros

--GIVEN--

$z = 1;
array_map($x => $x + 1, [1, 2, 3]);
array_map(($x) => $x + 1, [1, 2, 3]);
array_map($x => $x + $z, [1, 2, 3]);
array_map(($x) => $x + $z, [1, 2, 3]);

array_map(($x, $y) => $x + $y + $z, [1, 2, 3], [1, 2, 3]);

array_map(($x, $y, $z) => $x . strtoupper($y . $z), ['a', 'b'], ['a', 'b'], ['a', 'b']);

--EXPECT--

$z = 1;
array_map(function ($x) {
    return $x+1;
}, [1, 2, 3]);
array_map(function ($x) {
    return $x+1;
}, [1, 2, 3]);
array_map([$z = $z ?? null, 'fn' => function ($x) use (&$z) {
    return $x+$z;
}]['fn'], [1, 2, 3]);
array_map([$z = $z ?? null, 'fn' => function ($x) use (&$z) {
    return $x+$z;
}]['fn'], [1, 2, 3]);

array_map([$z = $z ?? null, 'fn' => function ($x, $y) use (&$z) {
    return $x+$y+$z;
}]['fn'], [1, 2, 3], [1, 2, 3]);

array_map(function ($x, $y, $z) {
    return $x.strtoupper($y.$z);
}, ['a', 'b'], ['a', 'b'], ['a', 'b']);