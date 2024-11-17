using System;
using System.Diagnostics;

class Program
{
    static void Main(string[] args)
    {
        string scriptPath1 = "/Users/shamshasan/SchoolFolders/operatingSystems/CPU-Simulator-GUI/Scripts/fcfs_scheduling.py";
        string scriptPath2 = "/Users/shamshasan/SchoolFolders/operatingSystems/CPU-Simulator-GUI/Scripts/round_robin_scheduling.py";
        string pythonExecutable = "python3";

        ExecutePythonScript(scriptPath1, pythonExecutable);
        ExecutePythonScript(scriptPath2, pythonExecutable);
    }

    static void ExecutePythonScript(string scriptPath, string pythonExecutable)
    {
        ProcessStartInfo startInfo = new ProcessStartInfo
        {
            FileName = pythonExecutable,
            Arguments = scriptPath,
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            UseShellExecute = false,
            CreateNoWindow = true
        };

        Process process = new Process { StartInfo = startInfo };
        process.Start();
        string output = process.StandardOutput.ReadToEnd();
        string errors = process.StandardError.ReadToEnd();
        process.WaitForExit();

        Console.WriteLine($"Output from script {scriptPath}:");
        Console.WriteLine(output);

        if (!string.IsNullOrEmpty(errors))
        {
            Console.WriteLine($"Errors from script {scriptPath}:");
            Console.WriteLine(errors);
        }
    }
}
