from scipy.optimize import minimize



def f(x):
    return x**2
for P in np.array([[0.5, 2],
                   [2, 2],
                   [-1, 2],
                   [-2, 2],
                   [0, 0.5],
                   [0, -0.5]]):
    
    def objective(X):
        X = np.array(X)
        return np.linalg.norm(X - P)

    def c1(X):
        x,y = X
        return f(x) - y

    sol = minimize(objective, x0=[P[0], f(P[0])], constraints={'type': 'eq', 'fun': c1})
    X = sol.x

    print(f'The minimum distance is {objective(X):1.2f}. Constraint satisfied = {sol.status < 1e-6}')

    # Verify the vector to this point is normal to the tangent of the curve
    # position vector from curve to point
    v1 = np.array(P) - np.array(X)
    # position vector
    v2 = np.array([1, 2.0 * X[0]])
    print('dot(v1, v2) = ', np.dot(v1, v2))

    x = np.linspace(-2, 2, 100)

    plt.plot(x, f(x), 'r-', label='f(x)')
    plt.plot(P[0], P[1], 'bo', label='point')
    plt.plot([P[0], X[0]], [P[1], X[1]], 'b-', label='shortest distance')
    plt.plot([X[0], X[0] + 1], [X[1], X[1] + 2.0 * X[0]], 'g-', label='tangent')
    plt.axis('equal')
    plt.xlabel('x')
    plt.ylabel('y')
