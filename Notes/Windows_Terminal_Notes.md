# Windows Terminal Notes

Created: June 1, 2024 2:46 PM

## Quick Notes

## What is the Terminal

The terminal is the text based user interface of your computer. Anything you can do with your computer by clicking around can probably be done quicker and easier with the terminal, if you know how to use it. The limiting factor is almost always your own knowledge and it can take a very long time to learn, so practice often, record your findings, and keep learning. Windows actually has 2 different options for terminals. PowerShell is the newer terminal and is what you will most likely encounter. Command Prompt or cmd is the legacy terminal and while less common you should still attempt to familiarize yourself with it as you are likely to see it used in older tutorials or projects.

## PowerShell

PowerShell uses it’s own unique command line shell and scripting language. Commands are called “cmdlets” (pronounced “command-lets”). The scripting language is object oriented and is built on the .NET framework, giving it access to all the .NET libraries. Cmdlets follow a Verb-Noun naming structure, e.g., “Get-Help” or “Set-ExecutionPolicy”.  PowerShell’s pipelining is object oriented meaning objects, not text, are passed between commands. PowerShell comes with a bunch of different cmdlets and also allows you to make your own.

## Parts of a Command

### 1. Cmdlet

A cmdlet (pronounced "command-let") is a lightweight command used in the PowerShell environment. It follows the Verb-Noun naming convention.

- **Example**: `Get-Process`
    - **Verb**: `Get` - The action to be performed.
    - **Noun**: `Process` - The object that the action is being performed on.

### 2. Parameters

Parameters are used to pass data and options to cmdlets, functions, and scripts. They modify the behavior of the cmdlet.

- **Syntax**: (Starts with - if not required)`ParameterName ParameterValue`
- **Example**: `-Name "notepad"`
    - **Parameter Name**: `-Name`
    - **Parameter Value**: `"notepad"`

### 3. Arguments

Arguments are the values provided to the parameters. They specify what the parameter should act upon.

- **Example**: `"notepad"` in `Name "notepad"`

### 4. Pipeline

The pipeline (`|`) is used to pass the output of one cmdlet as input to another cmdlet. This allows for chaining commands together to perform complex tasks.

- **Syntax**: `InitialFunction | RecivingFunction`
- **Example**: `Get-Process | Where-Object { $_.CPU -gt 100 }`
    - The output of `Get-Process` is passed to `Where-Object`.

### 5. Script Block

A script block is a collection of statements or expressions that are enclosed in curly braces `{}`. It is used to define the actions to be performed.

- **Example**: `{ $_.CPU -gt 100 }` in `Where-Object { $_.CPU -gt 100 }`
    - The script block contains the condition to filter processes.

### 6. Operators

Operators perform operations on variables and values. Common operators include comparison operators (`-eq`, `-ne`, `-gt`, `-lt`), logical operators (`-and`, `-or`), and assignment operators (`=`).

- **Example**: `gt` (greater than) in `{ $_.CPU -gt 100 }`

### 7. Variables

Variables are used to store data that can be referenced and manipulated within a script or command. They are prefixed with a `$`.

- **Example**: `$process` in `$process = Get-Process`

### 8. Commandlets and Functions

Functions are reusable blocks of code that can be defined and invoked by name. Cmdlets are built-in or custom commands that follow the Verb-Noun naming convention.

- **Example**: `Function Get-CustomData { <code> }`

### Basic Cmdlets

- **Get-Command**: Lists all available cmdlets.
- **Get-Help**: Provides help and documentation for cmdlets.
- **Get-Process**: Retrieves information about running processes.
- **Get-Service**: Retrieves the status of services on a machine.
- **Set-ExecutionPolicy**: Changes the user preference for the PowerShell script execution policy
    - Format: “Set-ExecutionPolicy <execution policy> (Optional Parameters)
    - Options for execution policy: Restricted, AllSigned, Remote Signed, and Unrestricted
    - Optional parameters:
        - -Scope: Specifies the scope (Process, CurrentUser, LocalMachine)
    - Example: Set-ExecutionPolicy Remote Signed -Scope CurrentUser

### Common Global Parameters

- **Verbose**
    - Provides additional details about the operation performed by the cmdlet.
    - Example: `Get-Process -Verbose`
- **Debug**
    - Provides debugging information.
    - Example: `Get-Process -Debug`
- **ErrorAction**
    - Specifies how the cmdlet responds to a non-terminating error.
    - Values: `Continue`, `Stop`, `SilentlyContinue`, `Inquire`, `Ignore`, `Suspend`
    - Example: `Get-Process -ErrorAction Stop`
- **ErrorVariable**
    - Stores error information in a specified variable.
    - Example: `Get-Process -ErrorVariable MyErrorVar`
- **WarningAction**
    - Specifies how the cmdlet responds to a warning message.
    - Values: `Continue`, `SilentlyContinue`, `Stop`, `Inquire`
    - Example: `Get-Process -WarningAction SilentlyContinue`
- **WarningVariable**
    - Stores warning information in a specified variable.
    - Example: `Get-Process -WarningVariable MyWarningVar`
- **OutVariable**
    - Stores output information in a specified variable.
    - Example: `Get-Process -OutVariable MyOutputVar`
- **OutBuffer**
    - Specifies the number of objects to buffer before calling the next cmdlet in the pipeline.
    - Example: `Get-Process -OutBuffer 10`
- **PipelineVariable**
    - Stores the current pipeline object in a specified variable for use in the command.
    - Example: `Get-Process | ForEach-Object { $_ - $PipelineVariable }`
- **WhatIf**
    - Shows what would happen if the cmdlet runs, without actually performing the action.
    - Example: `Stop-Process -Name "notepad" -WhatIf`
- **Confirm**
    - Prompts for confirmation before executing the cmdlet.
    - Example: `Stop-Process -Name "notepad" -Confirm`
- **Force**
    - Suppresses confirmation prompts.
    - Example: `Stop-Process -Name "notepad" -Force`

## Shortcuts

- **PowerShell:** Win+x then i
- **PowerShell Admin:** Win+x then a
- **Command Prompt**: Win+r then cmd

---

## Definitions

- **Command Line Shell:**
- **Object Oriented:**
- **.NET Framework:**
- **Cmdlet:**