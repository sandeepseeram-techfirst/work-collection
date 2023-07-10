import time

from opentelemetry.sdk._logs import (

    LogEmitterProvider,

    LogRecord,

    get_log_emitter_provider,

    set_log_emitter_provider,

)

if __name__ == "__main__":
 
    configure_log_emitter_provider()

    log_emitter = get_log_emitter_provider().get_log_emitter(

        "shopper",

        "0.1.2",

    )

    log_emitter.emit(

        LogRecord(

            timestamp=time.time_ns(),

            body="first log line",

        )

    )