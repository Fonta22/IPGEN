if ($args[1] -eq '-s') {
    py saveip.py $args[0]
} elseif ($args[0] -eq 'clear') {
    py saveip.py 0
} else {
    py createbot.py $args[0]
}