# Account Invoice Task & Button Customization (Odoo 18)

This module extends the core Odoo 18 Accounting (`account.move`) workflow to implement a strict financial control process and installment management.

## Features
1. **Custom Invoice Workflow:** Adds a new interim state `First Confirm` between `Draft` and `Posted`.
2. **Dynamic Header Buttons:** - Hides core `Post`/`Confirm` buttons during `Draft` state.
   - Shows the custom `First Confirm` button initially.
   - Restores the native `Confirm` button only when the invoice reaches the `First Confirm` stage.
3. **Installment Planner:** Automatically generates an installment schedule layout based on the number of installments and interval days specified by the accountant, properly handling rounding differences.
