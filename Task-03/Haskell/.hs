import System.IO

-- Function to check if a number is prime
isPrime :: Int -> Bool
isPrime num
    | num <= 1    = False
    | otherwise   = null [x | x <- [2..floor (sqrt (fromIntegral num))], num `mod` x == 0]

-- Function to find and print prime numbers up to n
findPrimesUpToN :: Int -> IO ()
findPrimesUpToN n = do
    putStrLn $ "Prime numbers up to " ++ show n ++ ":"
    mapM_ print [x | x <- [2..n], isPrime x]

main :: IO ()
main = do
    putStr "Enter a number (n): "
    hFlush stdout
    input <- getLine
    let n = read input :: Int

    if n < 2
        then putStrLn "Prime numbers start from 2."
        else findPrimesUpToN n
