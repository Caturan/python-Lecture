
"""
Suppose that you want to get some help from your friends to solve some questions.
You should send four questions to different four people at the same time and then wait for their
answers. The signature of the coroutine that you can use is

get_answer(friend: str, question: str) -> str.

You should run this coroutine with the data given below:
questions = [
"What is the best way to learn Python?",
"Code quality or fast development?",
"Why did I take this class?",
"Where did Bora find these questions?"
]
friends = ["Rossum", "Eich", "Backus", "Stroustrup"]
Write a coroutine with the name main and run it from __main__ block.
"""

import asyncio

async def get_answer(friend: str, question: str) -> str:
    # Simulate getting an answer from a friend
    await asyncio.sleep(2)
    return f"{friend}'s answer to '{question}'"

async def main():
    questions = [
        "What is the best way to learn Python?",
        "Code quality or fast development?",
        "Why did I take this class?",
        "Where did Bora find these questions?"
    ]
    friends = ["Rossum", "Eich", "Backus", "Stroustrup"]

    # Create a list to store the tasks for each question
    tasks = []

    # Start a coroutine for each question and each friend
    for question, friend in zip(questions, friends):
        task = asyncio.create_task(get_answer(friend, question))
        tasks.append(task)

    # Wait for all tasks to complete
    answers = await asyncio.gather(*tasks)

    # Print the answers
    for answer in answers:
        print(answer)

if __name__ == "__main__":
    asyncio.run(main())



"""
Write the decorator with the
name MakeThreads which creates desired number
of threads from a function as given in the code
below.

@MakeThreads(4)
def main():
t = threading.current_thread().name
print(f"Hi from {t}")
"""

import threading

def MakeThreads(num_threads):
    def decorator(func):
        def wrapper(*args, **kwargs):
            threads = []

            # Define a function to be executed by each thread
            def thread_function():
                func(*args, **kwargs)

            # Create and start the threads
            for _ in range(num_threads):
                thread = threading.Thread(target=thread_function)
                threads.append(thread)
                thread.start()

            # Wait for all threads to finish
            for thread in threads:
                thread.join()

        return wrapper

    return decorator

# Applying the decorator to the main function with 4 threads
@MakeThreads(4)
def main():
    t = threading.current_thread().name
    print(f"Hi from {t}")

# Run the decorated main function
if __name__ == "__main__":
    main()
