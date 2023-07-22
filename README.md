# ProxyLLM - Proxy Classes for Language Models

The goal of ProxyLLM is providing python library that enables developers to effortlessly interface with various LLMs such as OpenAI's GPT-4, Google's BERT, and others. 

This package encapsulates the complex interactions with these LLMs behind intuitive and user-friendly proxy classes, allowing developers to focus on leveraging the power of these advanced models, without being bogged down by intricate API details and interfacing code.

## Features (WIP)

1. **Multiple LLM Support:** The package supports multiple LLMs, including but not limited to GPT-4, BERT, and others. It is also designed with flexibility in mind to accommodate future models.

2. **Uniform API:** It provides a uniform API for different LLMs, allowing developers to switch between models without the need to extensively change the codebase.

3. **Error Handling:** It includes built-in error handling and retry logic, ensuring that your application remains resilient against minor network hiccups and transient errors.

4. **Optimized Performance:** With caching and other optimizations, this package makes sure you get the best possible performance out of your chosen LLM.

5. **Asynchronous Support:** For developers who require high performance and non-blocking code execution, this package offers asynchronous methods.

## Installation

You can install the `proxyllm` package via pip:

```bash
pip install proxyllm
```

## Quickstart

Here's an example of how to create a ChatGPT proxy and use it to generate text:

```python
import proxyllm

session = proxyllm.Session()
while (prompt := input("you : ")) != "exit":
    message = session.send(prompt)
    print(f"\n{message['role']} : {message['content']}\n")
```

## Documentation

For detailed information on using this package, please refer to our [documentation](link_to_documentation).

## Contributing

We welcome contributions! Please see our [contributing guidelines](link_to_contributing_guidelines) for details.

## License

This project is licensed under the terms of the MIT license. See [LICENSE](link_to_license) for more details.
